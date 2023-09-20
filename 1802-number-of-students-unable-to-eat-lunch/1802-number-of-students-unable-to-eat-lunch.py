class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
    
        no_progress_count = 0
        # In this question we need to check if students consiquitvely fail to get sandwiched for len(students that is the nmax time)
        while no_progress_count < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                no_progress_count = 0  # Reset the count of no progress
            else:
                students.append(students.pop(0))
                no_progress_count += 1  # Increment the count of no progress
            

        return len(students)