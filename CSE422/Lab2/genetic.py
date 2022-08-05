import random

Batsman = 8
Target = 330
# genome = '10101010'
Size = 20
input_list = [('Tamim', 68), ('Shoumyo', 25), ('Shakib', 70), ('Afif', 53), ('Mushfiq', 71), ('Liton', 55),
              ('Mahmadullah', 66), ('Shanto', 29)]


class Genome(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        fitness = 0
        for i, val in enumerate(input_list):
            if self.chromosome[i] == '1':
                fitness = fitness + val[2]

        if fitness > Target:
            return 0
        return fitness

    @classmethod
    def mutated_genome(self):
        sequence = random.choices(['0', '1'])
        return sequence

    @classmethod
    def create_genome(self):
        global Batsman
        return [self.mutated_genome() for _ in range(Batsman)]

    def mutation(self, sp2):
        new_child = []
        for gene1, gene2 in zip(self.chromosome, sp2.chromosome):
            probability = random.random()

            if probability < 0.5:
                new_child.append(gene1)

            elif probability < 0.90:
                new_child.append(gene2)

            else:
                new_child.append(self.mutated_genome)

        return Genome(new_child)

    def crossover(self, sp2):
        cross_point = random.randint(0, Target)
        new_child1 = self.chromosome[:cross_point] + sp2.chromosome[cross_point:]

        new_child2 = self.chromosome[cross_point:] + sp2.chromosome[:cross_point]

        return new_child1, new_child2


#
# def generate_genome():
#     global Batsman
#     return random.choices([0, 1], k=Batsman)
#
# def generate_population():
#     global Size
#     return [generate_genome() for _ in range(Size)]

def main():
    number_sequence = []
    global Size
    is_number = False
    run_time = 1

    for _ in range(Size):
        sequences = Genome.create_genome()
        number_sequence.append(Genome(sequences))

    while not is_number:
        number_sequence = sorted(number_sequence, key=lambda x: x.fitness)

        if number_sequence[0].fitness == 330:
            is_number = True
            print(number_sequence[0])
            break

        new_number_sequence = []

        n = int((20 * Size) / 100)
        new_number_sequence.extend(number_sequence[:n])

        n = int((40 * Size) / 100)

        for _ in range(n):
            spouce1 = random.choice(number_sequence[:10])
            spouce2 = random.choice(number_sequence[:10])
            child1, child2 = spouce1.mutation(spouce2)
            new_number_sequence.extend([child1, child2])

        number_sequence = new_number_sequence


if __name__ == '__main__':
    main()