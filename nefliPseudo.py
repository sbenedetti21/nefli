class Contenido {
  int idVideo;
  double minutoActual;

  getIDVideo(){ return idVideo };
  getMinutoInicio(){ return minutoInicio };
}

class ServicioNefli {
    List<int> videos;
    List<Usuario> usuarios;
    Reproductor reproductor;

    agregarUsuario(Usuario usuario) {
        usuarios.add(usuario);
    }

    reproducirContenido(int idVideo) {
        if (videos.contains(idVideo)) {
            reproductor.play(idVideo, 0);
        } else {
            throw new VideoInexistenteException();
        }
    }

    reproducirContenido(int idVideo) {
        if (videos.contains(idVideo)) {
            reproductor.stop();
        } else {
            throw new VideoInexistenteException();
        }
    }

}

class Usuario {
    List<Contenido> contenidosEmpezados;
    ServicioNefli nefli;

    Usuario(ServicioNefli nefli) {
        this.nefli = nefli;
    }

    reproducirContenido(Contenido unContenido) {
        idVideo = unContenido.getIDVideo();
        nefli.reproducirContenido(idVideo);
    }

    pausarContenido(Contenido unContenido) {
        idVideo = unContenido.getIDVideo();
        nefli.pausarContenido(idVideo);
    }

    continuarViendo() {
        return contenidosEmpezados;
    }
}

------------------------------------------
Siento que tendría que ponerle un observador al usuario para saber cuando este quiere arrancar
un video o continuar viendo para a partir de eso llamar al reproductor, pero no se muy bien
como implementarlo.
Es raro porque es al contrario de como venimos viendo, que hay muchos observadores y un observado,
en este caso hay un observador y muchos observados.
