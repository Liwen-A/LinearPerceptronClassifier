import sys
import csv




def learn_weights(csv_path):
    """Learn attribute weights for a multiclass perceptron.

    Args:
        csv_path: the path to the input file.  The data file is assumed to have a header row, and
                  the class value is found in the last column.

    Returns: a dictionary containing the weights for each attribute, for each class, that correctly
            classify the training data.  The keys of the dictionary should be the class values, and
            the values should be lists attribute weights in the order they appear in the data file.
            For example, if there are four attributes and three classes (1-3), the output might take
            the form:
                { 1 => [0.1, 0.8, 0.5, 0.01],
                  2 => [0.9, 0.01, 0.05, 0.4],
                  3 => [0.01, 0.2, 0.3, 0.85] }
    """
    with open(csv_path,'r') as infile:
        reader = csv.reader(infile)
        attribute = next(reader)
        data = [row for row in reader]
    
    
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])
            
    domain = [list(set(x)) for x in zip(*data)]       
    weights ={}
    
    for i in domain[-1]:
        weights[i] = [0.0]*(len(attribute)-1) 
        
    while accuracy(weights,data) < 0.9:
       # print(accuracy(weights, data))
        for i in data:
            c = classify(weights, i)
            if c != i[-1]:
                wrong = [x[0]-x[1] for x in zip(weights[c],i[:-1]) ]
                correct = [x[0]+x[1] for x in zip(weights[i[-1]],i[:-1])]
                weights[c] = wrong
                weights[i[-1]] = correct
    
    return weights


def classify(weight,instance):
    """
    Given weight as dict, classify a given insance
    
    Args:
        weight: a dictionary, see learn_weights
        instance: a list as a data instance
        
    Returns: the label of this instance
    """
    c= []
    for j in weight.items():
        c.append((j[0],dot(j[1],instance[:-1])))
    return max(c,key = lambda x: x[1])[0]

def dot(x,y):
    """
    Calculate the dot product of two lists
    
    Args:
        x,y: two lists with equal length
    Returns:
        the dot product of x and y
    """
    r = 0
    for i in range(len(x)):
        r += x[i]* y[i]
    return r

def accuracy(weight,data):
    """
    calculate the accuracy of the weight on the given dataset
    
    Args:
        weight: a dict as weights
        data: dataset
    
    Returns: a float as the accuracy 
    """
    counter = 0
    for i in data:
        if classify(weight,i) == i[-1]:
            counter += 1
    return counter/len(data)
    """Given set of weights as dict, return accuracy"""





#############################################



if __name__ == '__main__':
    path_to_csv = sys.argv[1]
    class__weights = learn_weights(path_to_csv)
    for c, wts in sorted(class__weights.items()):
        print("class {}: {}".format(c, ",".join(wts)))







