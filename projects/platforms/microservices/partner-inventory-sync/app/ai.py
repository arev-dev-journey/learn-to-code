import json
from collections.abc import Sequence

import httpx

from .config import get_settings
from .models import QueueEvent


def summarize_failed_events(events: Sequence[QueueEvent]) -> tuple[str, str]:
    if not events:
        return 'No failed events in queue.', 'rules'

    settings = get_settings()
    excerpts = [
        {
            'id': event.id,
            'event_type': event.event_type,
            'error_message': event.error_message,
            'attempt_count': event.attempt_count,
        }
        for event in events[:20]
    ]

    if settings.llm_base_url and settings.llm_api_key:
        try:
            payload = {
                'model': settings.llm_model,
                'messages': [
                    {'role': 'system', 'content': 'You summarize backend queue failures for operators.'},
                    {
                        'role': 'user',
                        'content': f'Summarize the likely root causes and mitigations: {json.dumps(excerpts)}',
                    },
                ],
                'temperature': 0.2,
            }
            headers = {'Authorization': f'Bearer {settings.llm_api_key}'}
            with httpx.Client(timeout=10.0) as client:
                response = client.post(f'{settings.llm_base_url}/chat/completions', json=payload, headers=headers)
                response.raise_for_status()
                data = response.json()
            content = data['choices'][0]['message']['content']
            if content:
                return content.strip(), f'openai-compatible:{settings.llm_model}'
        except Exception:
            pass

    grouped = {}
    for event in excerpts:
        key = event['error_message'] or 'unknown error'
        grouped[key] = grouped.get(key, 0) + 1

    summary = '; '.join(f"{count}x {err}" for err, count in grouped.items())
    return f'Fallback summary of failures: {summary}.', 'rules'
