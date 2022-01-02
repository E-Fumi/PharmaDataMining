def find_from_formula(dataset_row):
    formula = dataset_row['Molecular Formula']
    if 'C' in formula:
        molecule_dictionary = {'C': 0, 'H': 0, 'N': 0, 'F': 0, 'Cl': 0, 'Br': 0, 'I': 0}
        molecule_dictionary = parse_formula(formula, molecule_dictionary)
        double_bond_equivalents = double_bond_equivalent_calculator(molecule_dictionary)
        return max(0, double_bond_equivalents)
    else:
        return 0


def parse_formula(formula, molecule_dictionary):
    for element in molecule_dictionary:
        index_list = [index for index in range(len(formula)) if formula.find(element, index) == index]
        for index in index_list:
            if index == (len(formula) - len(element)) or formula[index + len(element)].isupper():
                molecule_dictionary[element] += 1
            elif formula[index + len(element)].islower():
                pass
            elif formula[index + len(element)].isdigit():
                molecule_dictionary[element] += read_number(formula, index + len(element))
    molecule_dictionary = check_for_charge(molecule_dictionary, formula)
    return molecule_dictionary


def read_number(formula, index):
    nr_string = ''
    while index < len(formula):
        if formula[index].isdigit():
            nr_string += formula[index]
            index += 1
        else:
            break
    return int(nr_string)


def check_for_charge(molecule_dictionary, formula):
    if formula[-1] == '+':
        molecule_dictionary['H'] -= 1
    if formula[-1] == '-':
        molecule_dictionary['H'] += 1
    return molecule_dictionary


def double_bond_equivalent_calculator(dictionary):
    dbe = 1 + dictionary['C'] + (dictionary['N'] / 2)
    dictionary['X'] = dictionary['H'] + dictionary['F'] + dictionary['Cl'] + dictionary['Br'] + dictionary['I']
    dbe -= dictionary['X'] / 2
    return dbe
