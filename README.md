******************
##Categorical-Encode
******************

**Project Description**


This package can be used to convert dataset into numerical categorical data.
This can be utilized for the pre-processing of various kinds of data for many Machine Learning Models. There are various features available such as normalizing the data to make the data more useful for the model. This function will work on any kind of data in the DataFrame.


**IMPORT:**




**from categorical_encode.categorical import categorical**




**The Parameters:-**


- **dataframe**: The Input DataFrame(X) which you want to categorically encode.
- **normalize**: This parameter determines if it will be between 0-1(1 included) or 1 to no. of classes (1 - no. of classes). default:False
- **drop_columns**:  This specifies the dataframe columns that need to be dropped as they are useless. default: No Columns
- **drop_na**: This drops empty values (NaN) if is set to True. default: False
- **target_columns**: This creates the target DataFrame(Y) without applying any Encoding. default: No Columns

**Return**

This Returns Two DataFrame (X,Y) if target_columns are provided Else only the Input dataframe (X) which is encoded.

**Example:**

**from categorical_encode.categorical import categorical**

**df = categorical(dataframe = df, normalize= True)**


This returns df as categorically encoded column-wise for all the columns having values between 0-1(1 included).
