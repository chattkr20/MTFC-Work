import pandas as pd
import numpy as np

def main():
        dataframe = pd.read_excel("11428_0_teams_1664311385.xlsx")
        unique_causes = dataframe['Cause of Death'].unique()
        results = pd.DataFrame()
        
        # for cause in unique_causes:
        #         sub = dataframe[dataframe['Cause of Death'] == cause]
        #         #print(cause, ": ", sub['Deaths'].sum())
        #         #results = pd.DataFrame(np.append(results, np.array([cause, sub['Deaths'].sum()])))
        #         #results = results.append([[cause, sub['Deaths'].sum()]])
        #         results = pd.concat([results, pd.DataFrame([[cause, sub['Deaths'].sum()]])])
        #         #np.append(results, 4)

        # #results = np.sort(results['Deaths'])
        # results.columns = ['Name', 'Deaths']
        # #print(results)
        # print(float(results[results['Name'] == 'COVID-19 (U07.1)']['Deaths']) / 20.0)

        print(dataframe.groupby(['Cause of Death']).sum().sort_values('Deaths', ascending = False))

if __name__ == "__main__":
    main()