import git
import os 
import random
import time
from ortools.algorithms.python import knapsack_solver

def Solver(file):
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    values = []
    weights = [[]]
    capacities = []
    with open(file, 'r') as kp_file:
        lines = kp_file.readlines() 
        capacities = [int(lines[2].strip())]
        values = [int(line.split()[0]) for line in lines[4:]]  
        weights[0] = [int(line.split()[1]) for line in lines[4:]] 
    
    solver.set_time_limit(180) 
    
    solver.init(values, weights, capacities)
    
    start_time = time.time()
    computed_value = solver.solve()
    elapsed_time = time.time() - start_time
    
    packed_items = []
    packed_weights = []
    total_weight = 0
    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]

    old_path = file
    new_path = old_path.replace('kplib', 'Result')
    new_path = new_path.replace('.kp', '_res.txt')
    optimal = False
    if elapsed_time < 180.0:
        optimal = True
    if not os.path.exists(os.path.dirname(new_path)):
        os.makedirs(os.path.dirname(new_path))
    if not os.path.exists(new_path):
        with open(new_path, 'w') as result:
            result.write("Time: {}s\n".format(elapsed_time))
            result.write('Capacity: {}\n'.format(capacities))
            result.write("Total value: {}\n".format(computed_value))
            result.write("Total weight: {}\n".format(total_weight))
            result.write("Packed items: {}\n".format(packed_items))
            result.write("Packed weights: {}\n".format(packed_weights))
            result.write("Optimal: {}\n".format(optimal))
            
current_directory =  os.getcwd()
if not os.path.exists(current_directory + '\kplib'):
    git.Git(current_directory).clone(
        "https://github.com/likr/kplib.git"
    )
    
folder_path = current_directory + '\kplib'
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir() and os.path.basename(f.path) != '.git']
for subfolder in subfolders:

    sub_subfolders = [f.path for f in os.scandir(subfolder) if f.is_dir()]
    for sub_subfolder in sub_subfolders:
        sub_sub_subfolders = [f.path for f in os.scandir(sub_subfolder) if f.is_dir()]
        for sub_sub_subfolder in sub_sub_subfolders:
            kp_files = [f.path for f in os.scandir(sub_sub_subfolder) if f.is_file()]
            random_files = random.sample(kp_files, 5)

            for file in random_files:
                Solver(file)

