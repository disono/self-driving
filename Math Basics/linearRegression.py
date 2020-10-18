import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# y = dependent variable
# x = independent variable
data = {
        'x': [69, 63, 66, 64, 67, 64, 70, 66, 68, 67, 65, 71],
        'y': [70, 65, 68, 65, 69, 66, 68, 65, 71, 67, 64, 72]
}


dataFrame = pd.DataFrame(data=data)


x = dataFrame.x
y = dataFrame.y


model = np.polyfit(x, y, 1)
m, b = np.polyfit(x, y, 1)
print(m, b)

predict = np.poly1d(model)
yPredict = 50
print(predict(yPredict))
print(model)


# generate plot of points
plt.scatter(x, y)
plt.show()
