def perform_iterations(multiple, limit):

    counter = 0

    while counter <= limit - multiple:
        counter += multiple
        print(counter)

perform_iterations(7, 100)
perform_iterations(8, 200)
perform_iterations(9, 300)



