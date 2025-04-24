def check_inclusion_array(s1:str, s2:str) -> bool:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.

     

    Example 1:

    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
    Example 2:

    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false
     

    Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
    """

    if len(s1) > len(s2): return False
    
    window_size: int = len(s1)
    # char frequency counter based on alphabet. Initialized to 0
    s1_counts: list = [0] * 26 
    s2_counts: list = [0] * 26

    for i in range(len(s1)):
        # Update char frequency based on s1
        s1_counts[ord(s1[i]) - ord('a')] += 1
        s2_counts[ord(s2[i]) - ord('a')] += 1

    if s1_counts == s2_counts: return True

    for i in range(window_size, len(s2)):
        # Update char frequency based on the window_size as we iterate through s2
        # Increase frequency
        s2_counts[ord(s2[i]) - ord('a')] += 1 #
        # Decrease frequency if out of window_size
        s2_counts[ord(s2[i - window_size]) - ord('a')] -= 1

        # Check if counts are similar
        if s2_counts == s1_counts: return True


    return False
