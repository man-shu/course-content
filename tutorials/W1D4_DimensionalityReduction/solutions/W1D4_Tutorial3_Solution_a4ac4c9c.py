
def get_variance_explained(evals):
  """
  Plots eigenvalues.

  Args:
    (numpy array of floats) : Vector of eigenvalues

  Returns:
    Nothing.

  """

  # Cumulatively sum the eigenvalues
  csum = np.cumsum(evals)

  return csum / np.sum(evals)


# Calculate the variance explained
variance_explained = get_variance_explained(evals)

# Visualize
with plt.xkcd():
  plot_variance_explained(variance_explained)