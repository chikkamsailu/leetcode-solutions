class Solution:
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1
        return image

        
