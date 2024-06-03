import matplotlib.pyplot as plt


def plot_results(data1, data2, result):
    """Plot the original datasets and the result."""
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    axs[0].imshow(data1, cmap='viridis')
    axs[0].set_title('Data 1')

    axs[1].imshow(data2, cmap='viridis')
    axs[1].set_title('Data 2')

    axs[2].imshow(result, cmap='viridis')
    axs[2].set_title('Result')

    plt.show()
