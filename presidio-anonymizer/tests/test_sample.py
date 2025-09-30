import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # replace the following line with your test
    first= {
        "text": "My name is Bip",
        "items": [
            {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
        ]
    }
    result = sample_run_anonymizer("My name is Bond",11,15)
    assert first.__eq__(result)
