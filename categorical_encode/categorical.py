
def categorical(
    dataframe=None,
    normalize=False,
    drop_columns=[],
    drop_na=False,
    target_columns=[],
              ):
    """
    :rtype: Pandas DataFrame
    :param dataframe: The Input DataFrame(X) which you want to categorically encode.
    :param normalize: This parameter determines if it will be between 0-1(1 included) or 1 to no. of classes (1 - no. of classes). default:False
    :param drop_columns:  This specifies the dataframe columns that need to be dropped as they are useless. default: No Columns
    :param drop_na: This drops empty values (NaN) if is set to True. default: False
    :param target_columns: This creates the target DataFrame(Y) without applying any Encoding. default: No Columns
    :return: This Returns Two DataFrame(X,Y) if target_columns are provided Else only the Input dataframe(X) which is encoded.
    """

    import pandas as pd
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError('Type Error : Expects pd.DataFrame for the parameter -> "dataframe"'
                         )
    if len(dataframe.columns) == 0:
        raise ValueError('Data Error : The parameter -> "dataframe" is empty'
                         )

    # This Drops the columns if columns are provided for the dataframe using parameter: drop_columns

    dataframe.drop(columns=drop_columns, inplace=True)

    # This drops empty values (NaN) if drop_na flag is set to True.

    dataframe.dropna(inplace=drop_na)

    # Initializes the target_dataframe

    target_dataframe = pd.DataFrame(dataframe[target_columns])

    # If target_columns is provided target_columns are not encoded and removed from the input dataframe.

    if len(target_columns) > 0:
        dataframe.drop(columns=target_columns, inplace=True)

    for i in dataframe.columns:
        lst = dataframe[i].unique()
        dic = dict(zip(lst, range(1, len(lst) + 1)))
        dataframe[i] = dataframe[i].map(dic)

        # The normalize flag determines if it will be between 0-1 or 1 to no. of classes (1 - no. of classes).

        if normalize:
            dataframe[i] /= len(lst)

    # If target_columns is provided then it is returned as a Dataframe(Y) along with Input Dataframe(X).

    if len(target_columns) > 0:
        return (dataframe, target_dataframe)
    else:
        return dataframe
