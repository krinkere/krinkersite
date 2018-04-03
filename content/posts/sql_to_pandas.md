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
table {
    border: 1px solid black;
}
td {
    border: 10px solid black;
}

</style>

<table>
    <tr>
            <th bgcolor="gray">SQL</th>
            <th bgcolor="gray">Pandas</th>
     </tr>
        <tr>
            <td>select * from airports</td>
            <td>airports</td>
        </tr>
        <tr>
            <td>select * from airports limit 3</td>
            <td>airports.head(3)</td>
        </tr>
        <tr>
            <td>select id from airports where ident = 'KLAX'</td>
            <td>airports[airports.ident == 'KLAX'].id</td>
        </tr>
        <tr>
            <td>select distinct type from airport</td>
            <td>airports.type.unique()</td>
        </tr>
        <tr>
            <td>select * from airports where iso_region = 'US-CA' and type = 'seaplane_base'</td>
            <td>airports[(airports.iso_region == 'US-CA') & (airports.type == 'seaplane_base')]</td>
        </tr>
        <tr>
            <td>select ident, name, municipality from airports where iso_region = 'US-CA' and type = 'large_airport'</td>
            <td>airports[(airports.iso_region == 'US-CA') & (airports.type == 'large_airport')][['ident', 'name', 'municipality']]</td>
        </tr>
        <tr>
            <td>select * from airport_freq where airport_ident = 'KLAX' order by type</td>
            <td>airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type')</td>
        </tr>        
        <tr>
            <td>select * from airport_freq where airport_ident = 'KLAX' order by type desc</td>
            <td>airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type', ascending=False)</td>
        </tr>        
        <tr>
            <td>select * from airports where type in ('heliport', 'balloonport')</td>
            <td>airports[airports.type.isin(['heliport', 'balloonport'])]</td>
        </tr>        
        <tr>
            <td>select * from airports where type not in ('heliport', 'balloonport')</td>
            <td>airports[~airports.type.isin(['heliport', 'balloonport'])]</td>
        </tr>         
        <tr>
            <td>select iso_country, type, count(&ast;) from airports group by iso_country, type order by iso_country, type</td>
            <td>airports.groupby(['iso_country', 'type']).size()</td>
        </tr>         
        <tr>
            <td>select iso_country, type, count(&ast;) from airports group by iso_country, type order by iso_country, count(&ast;) desc</td>
            <td>airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'], ascending=[True, False])</td>
        </tr>
        <tr>
            <td>select type, count(&ast;) from airports where iso_country = 'US' group by type having count(&ast;) > 1000 order by count(&ast;) desc</td>
            <td>airports[airports.iso_country == 'US'].groupby('type').filter(lambda g: len(g) > 1000).groupby('type').size().sort_values(ascending=False)</td>
        </tr>
        <tr>
            <td>select iso_country from by_country order by size desc limit 10</td>
            <td>by_country.nlargest(10, columns='airport_count')</td>
        </tr>
        <tr>
            <td>select iso_country from by_country order by size desc limit 10 offset 10</td>
            <td>by_country.nlargest(20, columns='airport_count').tail(10)</td>
        </tr>
        <tr>
            <td>select max(length_ft), min(length_ft), mean(length_ft), median(length_ft) from runways</td>
            <td>runways.agg({'length_ft': ['min', 'max', 'mean', 'median']})</td>
        </tr>
        <tr>
            <td>select airport_ident, type, description, frequency_mhz from airport_freq join airports on airport_freq.airport_ref = airports.id where airports.ident = 'KLAX'</td>
            <td>airport_freq.merge(airports[airports.ident == 'KLAX'][['id']], left_on='airport_ref', right_on='id', how='inner')[['airport_ident', 'type', 'description', 'frequency_mhz']]</td>
        </tr>        
        <tr>
            <td>
                create table heroes (id integer, name text);<br>
                insert into heroes values (1, 'Harry Potter');<br>
                insert into heroes values (2, 'Ron Weasley');<br>
                insert into heroes values (3, 'Hermione Granger');
            </td>
            <td>
                df1 = pd.DataFrame({'id': [1, 2], 'name': ['Harry Potter', 'Ron Weasley']})<br>
                df2 = pd.DataFrame({'id': [3], 'name': ['Hermione Granger']})<br>
                pd.concat([df1, df2]).reset_index(drop=True)
            </td>
        </tr>        
        <tr>
            <td>update airports set home_link = 'http://www.lawa.org/welcomelax.aspx' where ident == 'KLAX'</td>
            <td>airports.loc[airports['ident'] == 'KLAX', 'home_link'] = 'http://www.lawa.org/welcomelax.aspx'</td>
        </tr>
        <tr>
            <td>delete from lax_freq where type = 'MISC'</td>
            <td>
                lax_freq = lax_freq[lax_freq.type != 'MISC'<br>
                lax_freq.drop(lax_freq[lax_freq.type == 'MISC'].index)
            </td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
</table>