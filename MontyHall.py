
import sys
import random
import locale

class MontyHall(object):

    simulation_runs = 0
    simulations = []

    def __init__(self, simulation_count=0):
        self.simulation_runs = int(simulation_count)

    def run(self):
        print("Running %s Simulations..." % (locale.format("%d", self.simulation_runs, grouping=True)))
        for i in xrange(1, self.simulation_runs):
            current_simulation = Simulation()
            current_simulation.win_position = random.randint(1, 3)
            current_simulation.player_pick = random.randint(1, 3)
            self.simulations.append(current_simulation)
            # print("Player picked %d and winner is %d." % (current_simulation.player_pick, current_simulation.win_position))

        win_count = 0
        lose_count = 0

        for i in xrange(0, self.simulation_runs - 1):
            simulation_result = self.simulations[i]

            if simulation_result.win_position == simulation_result.player_pick:
                simulation_result.switch_wins = False
                lose_count += 1
            else:
                simulation_result.switch_wins = True
                win_count += 1
        print("\n-=/\ RESULT /\=-")
        print("Switch win count: %s - %.1f%%" % (locale.format("%d", win_count, grouping=True), ((float(win_count)/self.simulation_runs)*100)))
        print("Switch lose count: %s - %.1f%%" % (locale.format("%d", lose_count, grouping=True), ((float(lose_count)/self.simulation_runs)*100)))


class Simulation(object):
    win_position = None
    player_pick = None
    switch_wins = None

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'en_US')
    current_test=MontyHall(sys.argv[1])
    current_test.run()
