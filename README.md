### note: the $ is supposed to be ignored in the syntax, just type in the values 

# commands:
> <code>champion -d $year</code>
>
> driver's champion of that year 

> <code>champion -c $year</code>
>
> constructor's champion of that year

> <code>championship -d $year</code>
>
> the entire driver's championship of that year

> <code>championship -c $year</code>
>
> the entire constructor's championship of that year

> <code>at-pos -d $year $position</code>
>
> fetches the driver at that position in that year's championship

> <code>at-pos -c $year $position</code>
>
> fetches the constructor at that position in that year's championship

> <code>at-pos -q $year $position :$race:</code>
>
> fetches the driver at that qualifying position in that year at that race

> <code>races $year</code>
>
> races in that year's calendar 

> <code>winner $year :$race:</code>
>
> winner of that race in that year

> <code>pole $year :$race:</code>
>
> driver with pole position of that race in that year

> <code>qualifying $year :$race:</code> 
>
> the entire qualifying of that race in that year

## flags:

> <code>-!p</code>
>
> dont show points
>
> add to cmd championship

> <code>-p</code>
> 
> show points
>
> add to cmds champion, at-pos
