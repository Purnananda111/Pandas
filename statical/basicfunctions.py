import pandas as pd

student_marks = pd.DataFrame([[10,9,8,7],[9,4,5,6],[5,4,1,2]],columns=["Maths","Science","Telugu","English"],index=["Purna","Akhila","Sai"])
print(student_marks)
#mean of df which is avg

print("ave of each column ",student_marks.mean())
print("ave of each row ",student_marks.mean(axis=1))

#median()
#middle value of df which is avg

print("middle value of each column ",student_marks.median())
print("middle value  of each row ",student_marks.median(axis=1))
#std stand deviation rom median
print("stand deviation of each column ",student_marks.std())
print("stand deviation  of each row ",student_marks.std(axis=1))
#varience- square of stand deviation rom median
print("square of stand deviation of each column ",student_marks.var())
print("square of stand deviation  of each row ",student_marks.var(axis=1))

#min
print("min of student",student_marks.min())
#max
print("min of student",student_marks.max())
#mode most frequency value
print("mode of student",student_marks.mode())

