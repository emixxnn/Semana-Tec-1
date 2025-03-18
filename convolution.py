image = [[-1,1], 
        [-2, 2]]

kernel = [[3,1],
        [2,0]]

image_size = len(image)
kernel_size = len(kernel)

size_padd= image_size + kernel_size
image_padd = []

for _ in range(size_padd):
    row = []
    for _ in range(size_padd):
        row.append(0)
    image_padd.append(row)


for i in range(image_size):
    for j in range(image_size):
        image_padd[i + 1][j + 1] = image[i][j] 

output_size = size_padd - kernel_size + 1 
output = []

for _ in range(output_size):
    row = []
    for _ in range(output_size):
        row.append(0)
    output.append(row)

for i in range(output_size):
    for j in range(output_size):
        sum_value = 0  
        for ki in range(kernel_size):
            for kj in range(kernel_size):
                sum_value += image_padd[i + ki][j + kj] * kernel[ki][kj]
        output[i][j] = sum_value  

for row in output:
    print(row)

