"""This module is used for testing dataframes"""


def test_create_dataframe1(dataframe, columns_names):
    """
    Input: Dataframe and columns_names
    return values: Bool value(If dataframe satisfies the requirement then return True
    else return False
    """
    if dataframe.shape[0] < 10:
        return False

    # The DataFrame contains only the columns that you specified as the second argument.
    list(dataframe.columns).sort()
    columns_names.sort()
    if list(dataframe.columns) != columns_names:
        return False

    for i in list(dataframe.columns):
        for j in dataframe[i]:
            if type(j) != type(list(dataframe[i][0])):
                return False
    return True

def check_type(dataframe):
    """
    Check that all columns have values of the correct type.
    Input: Dataframe
    Output: Bool values(If all columns of the dataframe have values of the same type, return True;
    else return False
    """
    for i in list(dataframe.columns):
        for j in dataframe[i]:
            if type(j) != type(list(dataframe[i])[0]):
                return False
    return True

def detect_na(dataframe):
    """
    Check for nan values
    Input: Dataframe
    Output: Bool values(If there exists null value in the dataframe return True;
    else return False
    """
    df_bool = dataframe.isna()
    for col in df_bool.columns:
        if True in list(df_bool[col]):
            return False
    return True

def check_row_num(dataframe):
    """
    Verify that the dataframe has at least one row
    Input:dataframe
    Output: Bool values(If the dataframe has at least one row, return True;
    else return False
    """
    if dataframe.shape[0] < 1:
        return False
    return True

def test_check_rownum(dataframe):
    """Test check_row_num function"""
    value = check_row_num(dataframe)
    assert value

def test_detect_na(dataframe):
    """Test detect_na function"""
    value = detect_na(dataframe)
    assert value

def test_check_type(dataframe):
    """Test check_type function"""
    value = check_type(dataframe)
    assert value
