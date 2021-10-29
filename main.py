
class Clock:
  def __init__(self, name):
    self.name = name
    self.time = 0

  def tick(self):
    self.time += 1

  def sendMessage(self, clock):
    self.tick()
    clock.receiveMessage(self)

  def receiveMessage(self, clock):
    self.time = max(self.time, clock.time)
    print("[{}] Clock {} received message from clock {}".format(self.time, self.name, clock.name))

def main():
  clock1 = Clock("1")
  clock2 = Clock("2")
  clock3 = Clock("3")
  clock1.sendMessage(clock2)
  clock2.sendMessage(clock3)
  clock3.sendMessage(clock1)
  clock1.sendMessage(clock3)

if __name__ == '__main__':
  main()
