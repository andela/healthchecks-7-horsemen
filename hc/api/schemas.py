check = {
    "properties": {
        "name": {"type": "string"},
        "tags": {"type": "string"},
        "timeout": {"type": "number", "minimum": 60, "maximum":  29030400},
        "grace": {"type": "number", "minimum": 60, "maximum":  29030400},
        "nag_interval": {"type": "number", "minimum": 60, "maximum": 604800},
        "nag_status_on": {"type": "boolean"},
        "channels": {"type": "string"}
    }
}
