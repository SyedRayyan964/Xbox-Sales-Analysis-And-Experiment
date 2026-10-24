import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as mp

class Xbox_sales_analysis:
   def __init__(self):
    self.df=pd.read_csv("C:\\Users\\DELL\\Downloads\\Microsoft_data.csv")
    print(self.df)
   def old_data_analysis(self):
     # Profit made over months
     X_axis=self.df["Months"]
     Y_axis=self.df["Revenue"]
     mp.subplot(3,2,1)
     mp.plot(X_axis,Y_axis,marker="o")
     mp.xlabel("Months")
     mp.ylabel("Revenue in Millions")
     mp.title("Revenue over months.")
     mp.grid()
     # Unit sold over months
     X_axis=self.df["Months"]
     Y_axis=self.df["Total Sold"]
     mp.subplot(3,2,2)
     mp.bar(X_axis,Y_axis,color="r",edgecolor="black")
     mp.xlabel("Months")
     mp.ylabel("Unit sold")
     mp.title("Unit sold over months")
     mp.grid(axis="y")
     # traffic over months
     percents=[35,32,37,34,40,43,46,42,39,45,60,70]
     Labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
     explode=[0,0,0,0,0,0,0,0,0,0,0,0.1]
     colors = ["red","blue","green","yellow","orange","purple","pink","black","white","brown","gray","cyan"]
     mp.subplot(3,2,5)
     mp.pie(percents,labels=Labels,shadow=True,explode=explode,colors=colors)
     mp.title("Traffic over months")
     # loses vs profit in months
     X_axis=self.df["Months"]
     Y_axis_1=self.df["Revenue"]
     Y_axis_2=self.df["Loss"]
     mp.subplot(3,2,6)
     mp.scatter(X_axis,Y_axis_1,color="red",label="Profit")
     mp.scatter(X_axis,Y_axis_2,color="blue",label="Loss")
     mp.xlabel("Months")
     mp.ylabel("Profit/Loss in millions")
     mp.title("Loss vs Profit over months")
     mp.legend()
     mp.grid()
     mp.suptitle("Xbox 2026 Sales analysis")
     mp.show()
   def Exp_data_analysis(self):
     df=pd.read_csv("C:\\Users\\DELL\\Downloads\\Microsoft_data.csv")
    # Label encoding
     lb=LabelEncoder()
     df["Months"]=lb.fit_transform(df["Months"])

    # Feature Scaling
     FS=StandardScaler()
    # No need

    # train test split data
     X=df[["No.promotions","No.game releases","Months"]]
     y=df[["Loss","Revenue","Total Sold","Total Not Sold"]]
     X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,train_size=0.9)
    # Model training
     model=LinearRegression()
     model.fit(X_train,y_train)
     pred=model.predict(X_test)
     print("Prediction: ")
     print(pred)
     print("Actual value: ")
     print(y_test)
     print("Model accuracy is: ",model.score(X_test,y_test)*100)
     new_data={
        "No.promotions":[4,3,4,4,5,5,6,5,6,6,7,9],
        "No.game releases":[1,1,2,1,2,3,3,2,2,3,3,4],
        "Months":[4,3,7,0,8,6,5,1,11,10,9,2],
     }
     d_f=pd.DataFrame(new_data)
     new_prediction=model.predict(d_f[["No.promotions","No.game releases","Months"]])
     d_f=pd.DataFrame(new_prediction,columns=["Loss","Revenue","Total Sold","Total Not Sold"])
     print("New Data Prediction: ")
     print(new_prediction)
    # Profit Made old data vs Exp data
     mp.subplot(3,2,1)
     mp.plot(self.df["Months"],self.df["Revenue"],label="Old Data",marker="o",linewidth=3)
     mp.plot(self.df["Months"],d_f["Revenue"],label="New Data",marker="o",linewidth=3)
     mp.xlabel("Months")
     mp.ylabel("Revenue in Millions")
     mp.title("Revenue over months")
     mp.legend()
     mp.grid()
    # Unit sold over months
     mp.subplot(3,2,2)
     mp.bar(self.df["Months"],d_f["Total Sold"],color="b",label="New Data",edgecolor="black")
     mp.bar(self.df["Months"],df["Total Sold"],color="r",edgecolor="black",label="Old Data")
     mp.xlabel("Months")
     mp.ylabel("Unit Sold")
     mp.title("Unit sold over months")
     mp.legend()
     mp.grid(axis="y")
    # Loss over months
     mp.subplot(3,2,5)
     mp.scatter(self.df["Months"],df["Loss"],color="r",label="Old Data")
     mp.scatter(self.df["Months"],d_f["Loss"],color="b",label="New Data")
     mp.xlabel("Months")
     mp.ylabel("Loss in Thousands")
     mp.title("Loss over months")
     mp.legend()
     mp.grid(axis="y")
  # Unit not sold over months
     mp.subplot(3,2,6)
     mp.plot(self.df["Months"],df["Total Not Sold"],marker="o",label="Old Data")
     mp.plot(self.df["Months"],d_f["Total Not Sold"],marker="o",label="New Data")
     mp.xlabel("Months")
     mp.ylabel("Total not sold")
     mp.title("Total not sold over month's")
     mp.legend()
     mp.grid(axis="both")
     mp.show()
Run=Xbox_sales_analysis()
Run.old_data_analysis()
Run.Exp_data_analysis()
