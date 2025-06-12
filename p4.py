class State:
    def on_event(self, event):
        raise NotImplementedError

class Locked(State):
    def on_event(self, event):
        if event == 'coin':
            return Unlocked()
        return self

class Unlocked(State):
    def on_event(self, event):
        if event == 'push':
            return Locked()
        return self

class Turnstile:
    def __init__(self):
        self.state = Locked()

    def handle(self, event):
        print(f"Event: {event}, State: {self.state.__class__.__name__}")
        self.state = self.state.on_event(event)

fsm = Turnstile()
events = ['coin', 'push', 'push', 'coin', 'coin']
for e in events:
    fsm.handle(e)
