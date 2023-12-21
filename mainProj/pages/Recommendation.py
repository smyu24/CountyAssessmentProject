import streamlit as st
def recommendation():
    st.write("RECOMMENDATION PAGE")
    temp="""
    https://github.com/ash2shukla/streamlit-bokeh-events
    This could be used to plot and add interactability with data/figuers 

    https://github.com/tvst/st-annotated-text
    This could be used to annotate text and provide definitions of technical jargon


    Housing Shortage Tracker
    Housing Affordability Index

    Freddie Mac House Price Index price appreciation from 1990 to 2023
    https://en.wikipedia.org/wiki/House_price_index
    https://en.wikipedia.org/wiki/Category:Real_estate_indices
    https://en.wikipedia.org/wiki/US_Commercial_Real_Estate_Index



    data = pd.read_csv('housesorted.csv',usecols =['price','tax','year','bedroom','bathroom','lot'],error_bad_lines=False )
    #sns.pairplot(data, x_vars=['tax','year','bedroom'], y_vars='price', size=7, aspect=0.8)
    #plt.show()
    data = data[['price','tax','year','bedroom','bathroom','lot']]
    x_vars=['tax','year','bedroom','bathroom','lot']

    X = data[x_vars]
    print type(X)

    y = data['price']

    X_train,X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    linreg = LinearRegression()
    model=linreg.fit(X, y)

    linear_model = sm.OLS(y,X)
    results = linear_model.fit()
    print results.summary()
    print linreg.intercept_

    B1,B2,B3,B4,B5 = linreg.coef_[0],linreg.coef_[1],linreg.coef_[2],linreg.coef_[3],linreg.coef_[4]
    print linreg.coef_
    x1,x2,x3,x4,x5 = input('input as: tax,year,bedroom,bathroom,lot')



    y_pred = B0 + B1*x1 + B2*x2 + B3*x3 + B4*x4 +B5*x5
    print 'y_pred=' + str(y_pred)





    Because there is no history deals information know about the accounts in the testset.we can't apply the Content based Filtering which used the user's historical behaviour and gave suggestions according to that.most suitable in this Cold start situation is the Collaborative Filtering and Hybrid Filtering which used the similarity between customers personal information to gave suggestions.

    Knn or nearest neighbour were used to find the similar Accounts.then get the properties those most similar customers have bought by using the mapping tables.In the last apply the Knn or nearest neighbour again,This time on the Properties to find the similar properties like that,we will recommend these properties to new Accounts.
(Clustering)
linear regression using multiple parameters to predict and get median absolute error prediction
    """