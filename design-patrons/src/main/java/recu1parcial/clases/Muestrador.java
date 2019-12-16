package recu1parcial.clases;

import javafx.beans.InvalidationListener;
import javafx.beans.Observable;


import java.util.List;

public class Muestrador implements Observable {
    private boolean estado;
    private List<String> datos;
    private String activacionFecha;

    private void activacion(){
        activacionFecha = "21/11/2019, 03:58:02";
        estado = true;
    }

    private void desactivavion(){
        estado = false;
    }


    @Override
    public void addListener(InvalidationListener listener) {

    }

    @Override
    public void removeListener(InvalidationListener listener) {

    }
}
