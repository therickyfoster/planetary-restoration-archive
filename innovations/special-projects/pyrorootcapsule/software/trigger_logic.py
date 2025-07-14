# Python script: Fires when soil temp exceeds threshold
def activate_capsule(temp):
    if temp >= 48:
        return 'Foam released'
    return 'Monitoring'