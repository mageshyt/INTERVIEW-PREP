        for source, dest in invocations:
            if not suspicious[source] and suspicious[dest]:
                removeAllowed = False
                break