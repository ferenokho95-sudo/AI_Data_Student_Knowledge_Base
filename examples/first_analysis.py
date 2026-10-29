"""Run from any working directory: python examples/first_analysis.py."""
from pathlib import Path
import pandas as pd


def analyze():
    source=Path(__file__).with_name('sales.csv')
    data=pd.read_csv(source)
    if data.isna().any().any():
        raise ValueError('В примере не должно быть пропусков')
    data['revenue']=data['quantity']*data['unit_price']
    result=data.groupby('product',as_index=False)['revenue'].sum().sort_values('revenue',ascending=False)
    assert len(data)==6
    assert data['revenue'].sum()==4100
    assert result.iloc[0]['product']=='Книга' and result.iloc[0]['revenue']==2000
    return data,result


if __name__=='__main__':
    data,result=analyze()
    print(result.to_string(index=False))
    print('Общая выручка:',data['revenue'].sum(),'руб.')
