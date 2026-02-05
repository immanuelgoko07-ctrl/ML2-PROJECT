@component(
    base_image="python:3.10",
    packages_to_install=["pandas", "prophet", "scikit-learn"]
)
def prophet_model(
    input_path: str,
    metrics_path: str
):
    import pandas as pd
    import numpy as np
    from prophet import Prophet
    from sklearn.metrics import mean_absolute_error, mean_squared_error

    df = pd.read_csv(input_path)
    df.rename(columns={'Year':'ds','Value':'y'}, inplace=True)

    # Train-test split
    train = df.iloc[:-5]
    test = df.iloc[-5:]

    model = Prophet(yearly_seasonality=True)
    model.fit(train)

    future = model.make_future_dataframe(periods=5, freq='Y')
    forecast = model.predict(future)

    preds = forecast.iloc[-5:]['yhat'].values

    mae = mean_absolute_error(test['y'], preds)
    rmse = np.sqrt(mean_squared_error(test['y'], preds))

    pd.DataFrame({
        "model": ["Prophet"],
        "MAE": [mae],
        "RMSE": [rmse]
    }).to_csv(metrics_path, index=False)

