# Lab3-DataVisualization

## Dataset

There are three datasets used in my assignment and all of them are about college salaries.

1. ***salaries-by-college-type.csv*** : It contains different types of salaries and their increase by type of college.
2. ***salaries-by-region.csv***: It contains different types of salaries and their increase by colleges in different regions.
3. ***degrees-that-pay-back.csv**: It contains different types of salaries and their increase by different majors.

## Data Analysis Task

I realize three data analysis tasks for my assignment.

### Visualize data by choosing visual encodings

I choose three types of visual encodings which are scatter, column and pie. The scatter graph is for ***Salaries by College Type*** and ***Salaries by Region*** . The column graph is for ***Salaries by Major Type***. The pie graph is for ***Number of Schools by College Type***.

![1](https://github.com/Easonrust/HCI_homework/blob/master/Lab3_DataVisualization/img/layout.png)

### Derive values of models from source data

For the pie graph, I calculate the numbers of Schools for every region and every college type and the code is as follows.

```  python
if dateset=='Salaries by Region':
        df=s_b_r
        Class='Region'
        return {
        'data': [go.Pie(
            labels=df[Class].unique(),
            values=[len(df[df[Class] == 'California']),len(df[df[Class] == 'Western']),len(df[df[Class] == 'Midwestern']),len(df[df[Class] == 'Southern']),len(df[df[Class] == 'Northeastern'])],
            hoverinfo='label+percent', textinfo='value',
            marker=dict(colors=['rgb(33, 75, 99)',
                                  'rgb(79, 129, 102)',
                                  'rgb(151, 179, 100)',
                                  'rgb(175, 49, 35)',
                                  'rgb(36, 73, 147)'])
        )],
        'layout': go.Layout(
            height=300,
            title='Number of Schools by Region',
        )
        }
    elif dateset=='Salaries by College Type':
        df=s_b_c_t
        Class='School Type'
        return {
        'data': [go.Pie(
            labels=df[Class].unique(),
            values=[len(df[df[Class] == 'Engineering']),len(df[df[Class] == 'Party']),len(df[df[Class] == 'Liberal Arts']),len(df[df[Class] == 'Ivy League']),len(df[df[Class] == 'State'])],
            hoverinfo='label+percent', textinfo='value',
            marker=dict(colors=['rgb(146, 123, 21)',
                                  'rgb(177, 180, 34)',
                                  'rgb(206, 206, 40)',
                                  'rgb(175, 51, 21)',
                                  'rgb(35, 36, 21)'])
        )],
        'layout': go.Layout(
            height=300,
            title='Number of Schools by College Type',
        )
        }
```

![1558968792744](https://github.com/Easonrust/HCI_homework/blob/master/Lab3_DataVisualization/img/pie1.png)

![1558968816064](https://github.com/Easonrust/HCI_homework/blob/master/Lab3_DataVisualization/img/pie2.png)

### Sort items to expose patterns

I set two dropdowns for my assignment and you can use them to choose based types for axises of the scatter graph.

![1558968993377](https://github.com/Easonrust/HCI_homework/blob/master/Lab3_DataVisualization/img/dropdown.png)

![1558969010781](https://github.com/Easonrust/HCI_homework/blob/master/Lab3_DataVisualization/img/changeSort.png)

![1558969039437](https://github.com/Easonrust/HCI_homework/blob/master/Lab3_DataVisualization/img/scatter.png)

## Layout and Patterns

### Layout

There are one tab and three dropdowns above three graphs.

![1](https://github.com/Easonrust/HCI_homework/blob/master/Lab3_DataVisualization/img/layout.png)

Patterns

1. For the scatter graph, I use different colors for different regions or different college types.
2. For the column graph, I use two colors for two salary types.
3. For the pie graph, I use different colors for different regions or different college types.
