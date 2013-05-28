BEGIN{
    FS=","
}
{
    if (seen[$2$3$4]) { 
        if (seen[$2$3$4]==$NF){
            print "dup" $2$3$4
        }else{
            print "nodup" seen[$2$3$4] $NF
        }
    } 
    seen[$2$3$4]=$NF
}

