var line = readline() 
var nums = line.split(' ')

var probabilities = [];

for (i = 1; i < nums[0] + nums[1]; i++) {
    probabilities[i] = 0;
}

for (i = 1; i < nums[0]; i++) {
    for (j = 1; j < nums[1]; j++) {
        probabilities[i + j]++;
    }
}

var multipleCorrect = false
max = probabilities[2]
maxIteration = 2
for (i = 2; i < nums[0] + nums[1]; i++) {
    if (probabilities[i] == max) {
        multipleCorrect = true
    } else if (probabilities[i] > max) {
        max = probabilities[i]
        maxIteration = i
        multipleCorrect = false
    } 
}

if (multipleCorrect) {
    for (i = 2; i < nums[0] + nums[1]; i++) {
        if (probabilities[i] == max) {
            print(i + 1)
        }
    }
} else {
    print(maxIteration + 1)
}