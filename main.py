from data_generator import generate_dataset
from operations import perform_broadcasting_operation
from visualization import plot_results


def main():
    # Here we generate random datasets
    data1 = generate_dataset((3, 4))
    data2 = generate_dataset((3, 1))

    # Lets perform broadcasting operation
    result = perform_broadcasting_operation(data1, data2)

    # Let's visualize the results
    plot_results(data1, data2, result)


if __name__ == "__main__":
    main()
