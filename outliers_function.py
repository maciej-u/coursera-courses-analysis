def identify_outliers(df):
    """
    Identifying outliers in a DataFrame using the Interquartile Range (IQR) method.

    Args:
        df (pandas.DataFrame): Input DataFrame containing numeric columns.

    Returns:
        pandas.DataFrame: A DataFrame containing the outliers. Each column in the
        returned DataFrame corresponds to a column in the input DataFrame and
        contains only the values identified as outliers for that column, with NaN
        for non-outlier entries.

    Notes:
        - This function is applying the IQR method to all numeric columns in the input DataFrame.
        - Outliers are being defined as values below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR,
          where Q1 is the first quartile, Q3 is the third quartile, and IQR is the
          interquartile range (Q3 - Q1).
        - The function is assuming all columns in the input DataFrame are numeric.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'A': [1, 2, 3, 4, 100], 'B': [1, 2, 3, 4, 5]})
        >>> outliers = identify_outliers(data)
        >>> print(outliers)
             A   B
        4  100 NaN
    """
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    IQR = q3 - q1
    outliers = df[((df < (q1 - 1.5 * IQR)) | (df > (q3 + 1.5 * IQR)))]
    return outliers