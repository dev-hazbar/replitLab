

function dirCreate(){
    NAME_INPUT=$1
    
    mkdir $NAME_INPUT
    touch $NAME_INPUT/{{input,output,info}.txt,$NAME_INPUT.py}
}

function elorion(){
    echo "Elorion, Beto!!!"
}