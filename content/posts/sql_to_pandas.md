Title: Mapping SQL to Pandas
Date: 2018-04-03 13:15
Modified: 2018-04-03 13:46
Status: published
Category: Python
Tags: python, pandas
Slug: mapping_sql_to_pandas
Authors: Al Krinker
Summary: Illustration of common SQL operations mapped to Pandas.

<style>
.table-borders td,
.table-borders th
{
    border: 1px solid black;
    padding: 10px;
}

span.bold-red {
    color: red;
    font-weight: bold;
}

</style>

<table class="table-borders">
    <tr>
            <th bgcolor="gray">SQL</th>
            <th bgcolor="gray">Pandas</th>
     </tr>
        <tr>
            <td>
                select<br>
                *<br>
                from table_name
             </td>
            <td>df</td>
        </tr>
        <tr>
            <td>
                select<br>
                *<br>
                from table_name<br>
                <span class="bold-red">limit</span> 3</td>
            <td>df.head(3)</td>
        </tr>
        <tr>
            <td>
                select<br>
                col_name_1<br>
                from table_name<br>
                <span class="bold-red">where</span> col_name_2 = 'value'</td>
            <td>df[df.col_name_2 == 'value'].col_name_1</td>
        </tr>
        <tr>
            <td>
                select<br>
                <span class="bold-red">distinct</span> col_name_1<br>
                from table_name</td>
            <td>df.col_name_1.unique()</td>
        </tr>
        <tr>
            <td>
                select<br>
                *<br>
                 from table_name<br>
                 where col_name_1 = 'val_1' <span class="bold-red">and</span> col_name_2 = 'val_2'</td>
            <td>df[(df.col_name_1 == 'val_1') & (df.col_name_2 == 'val_2')]</td>
        </tr>
        <tr>
            <td>select<br>
            col_name_1, col_name_3, col_name_3<br>
            from table_name<br>
            where col_name_4 = 'val_1' <span class="bold-red">and</span> col_name_5 = 'val_2'</td>
            <td>df[(df.col_name_4 == 'val_1') & (df.col_name_5 == 'val_2')][['col_name_1', 'col_name_2', 'col_name_3']]</td>
        </tr>
        <tr>
            <td>select<br>
            *<br>
            from table_name<br>
            where col_name_1 = 'value'<br>
            <span class="bold-red">order by</span> col_name_2</td>
            <td>df[df.col_name_1 == 'value'].sort_values('col_name_2')</td>
        </tr>
         <tr>
            <td>select<br>
            *<br>
            from table_name<br>
            where col_name_1 = 'value'<br>
            <span class="bold-red">order by</span> col_name_2 <span class="bold-red">desc</span></td>
            <td>df[df.col_name_1 == 'value'].sort_values('col_name_2', ascending=False)</td>
        </tr>        
        <tr>
            <td>select<br>
            *<br>
            from table_name<br>
            where col_name <span class="bold-red">in</span> ('val_1', 'val_2')</td>
            <td>df[df.col_name.isin(['val_1', 'val_2'])]</td>
        </tr>        
        <tr>
            <td>select<br>
            *<br>
            from table_name<br>
            where col_name <span class="bold-red">not in</span> ('val_1', 'val_2')</td>
            <td>df[~df.col_name.isin(['val_1', 'val_2'])]</td>
        </tr>   
        <tr>
            <td>select<br>
            col_name_1, col_name_2, count(&ast;)<br>
            from table_name<br>
            <span class="bold-red">group by</span> col_name_1, col_name_2<br>
            <span class="bold-red">order by</span> col_name_1, col_name_2</td>
            <td>df.groupby(['col_name_1', 'col_name_2']).size()</td>
        </tr>         
        <tr>
            <td>select<br>
            col_name_1, col_name_2, count(&ast;)<br>
            from table_name<br>
            <span class="bold-red">group by</span> col_name_1, col_name_2<br>
            <span class="bold-red">order by</span> col_name_1, count(&ast;) desc</td>
            <td>df.groupby(['col_name_1', 'col_name_2']).size().to_frame('size').reset_index().sort_values(['col_name_1', 'size'], ascending=[True, False])</td>
        </tr>      
        <tr>
            <td>select<br>
            col_name_1, count(&ast;)<br>
            from table_name<br>
            where col_name_2 = 'val_1'<br>
            group by col_name_1<br>
            <span class="bold-red">having</span> count(&ast;) > 1000<br>
            order by count(&ast;) desc</td>
            <td>df[df.col_name_2 == 'val_1'].groupby('col_name_1').filter(lambda g: len(g) > 1000).groupby('col_name_1').size().sort_values(ascending=False)</td>
        </tr>
        <tr>
            <td>select<br>
            col_name<br>
            from table_name<br>
            order by size<br>
            <span class="bold-red">desc limit</span> 10</td>
            <td>df.nlargest(10, columns='col_name')</td>
        </tr>
        <tr>
            <td>select<br>
            col_name<br>
            from table_name<br>
            order by size<br>
            <span class="bold-red">desc limit</span> 10
            <span class="bold-red">offset 10</span></td>
            <td>df.nlargest(<span class="bold-red">20</span>, columns='col_name').tail(10)</td>
        </tr>
        <tr>
            <td>select<br>
            <span class="bold-red">max</span>(col_name), <span class="bold-red">min</span>(col_name), <span class="bold-red">mean</span>(col_name), <span class="bold-red">median</span>(col_name)<br>
            from table_name</td>
            <td>df.agg({'col_name': ['min', 'max', 'mean', 'median']})</td>
        </tr>
        <tr>
            <td>select<br>
            col_name_1, col_name_2, col_name_3, col_name_4<br>
            from table_name_1<br>
            <span class="bold-red">join</span> table_name_2<br>
            on table_name_1.col_name_id_1 = table_name_2.col_name_id_2<br>
            where table_name_2.col_name = 'val'</td>
            <td>df1.merge(df2[df2.col_name == 'val'][['col_name_id_2']], left_on='col_name_id_1', right_on='col_name_id_2', how='inner')[['col_name_1', 'col_name_2', 'col_name_3', 'col_name_4']]</td>
        </tr>        
        <tr>
            <td>
                <span class="bold-red">create</span> table table_name (col_name_1 integer, col_name_2 text);<br>
                <span class="bold-red">insert</span> into table_name values (1, 'val_1');<br>
                insert into table_name values (2, 'val_2');<br>
                insert into table_name values (3, 'val_3');
            </td>
            <td>
                df1 = pd.DataFrame({'id': [1, 2], 'name': ['val_1', 'val_2']})<br>
                df2 = pd.DataFrame({'id': [3], 'name': ['val_3']})<br>
                pd.concat([df1, df2]).reset_index(drop=True)
            </td>
        </tr>        
        <tr>
            <td><span class="bold-red">update</span><br>
            table_name<br>
            set col_name_1 = 'val_1'<br>
            where col_name_2 == 'val_2'</td>
            <td>df.loc[df['col_name_2'] == 'val_2', 'col_name_1'] = 'val_1'</td>
        </tr>
        <tr>
            <td><span class="bold-red">delete</span><br>
            from table_name<br>
            where col_name = 'val'</td>
            <td>
                df = df[df.col_name != 'val'<br>
                df.drop(df[df.col_name == 'val'].index)
            </td>
        </tr>
</table>
