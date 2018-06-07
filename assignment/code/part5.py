from assignment import *

def main():
    # -----
    # 1. Load the list of 100 most frequent words from Part I.
    # 2. Load the context dictionary using the load_pkl function.
    # 3. Compute the spectral word embeddings for the top 100 words.
    # 3. Create a text file called top_100_dist.txt, with 100 lines, each line
    #    corresponding to a word on the same line in the top_100_list.txt file.
    #    The top_100_sim.txt file should contain a series of 100 floating point
    #    numbers in each line (10000 numbers total). The numbers should be your
    #    computed spectral distances to each of the words in the
    #    top_100_list.txt. This means the diagonal numbers should all be 0.0,
    #    and a number in row i, column j should represent the distance from the
    #    ith to the jth word in the top_100_list.txt loaded in step 1. Use your
    #    Use your implementation of the word_distance function.
    # 4. Answer the question: Which method of finding nearest neighbors do you
    #    suspect might be better in general (context similarity of spectral
    #    distance)? Why? Why do you think the results in this particular
    #    exercise might favor the similarity method (think data size used).
    #
    # YOUR CODE GOES HERE
    #
    # YOUR ANSWERS GO HERE
    # -----

if __name__ == "__main__":
    main()
