def max_marks_with_forgetfulness(chapters, total_time):
    """
    Calculate the maximum marks Chef can score in the exam given the constraints.

    Parameters:
    - chapters (list of tuples): Each tuple contains (marks, time) for a chapter.
    - total_time (int): Total time left before the exam.

    Returns:
    - int: The maximum marks Chef can score.
    """
    n = len(chapters)
    dp = [[0, -float('inf')] for i in range(total_time + 1)]
    
    for i in range(n):
        (m, t) = chapters[i]
        for j in range(total_time, t - 1, -1):
            dp[j][0] = max(dp[j - t][0] + m, dp[j][0])
            dp[j][1] = max(dp[j][1], dp[j - t][0], dp[j - t][1] + m)
    
    return dp[total_time][1]