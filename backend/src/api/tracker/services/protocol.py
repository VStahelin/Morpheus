from api.tracker.models import Protocol


def get_entries_by_user(protocol_id: int, user_id: int, date_from, date_to):
    protocol = Protocol.objects.get(id=protocol_id)
    entries = protocol.get_exercises_entries_by_user(
        protocol=protocol, user_id=user_id, date_from=date_from, date_to=date_to
    )
    return entries
