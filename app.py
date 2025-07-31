import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

class ServidorMagico:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def activar(self, sigilo, egregor, usuario, descripcion):
        st.write(f"¡Activando el servidor mágico {self.nombre} para {usuario}!")
        st.write(f"Sigilo cosmico generado en letras: {sigilo}")
        st.write("Construyendo sigilo mágico para generar el huevo magico...")
        visualize_sigil(sigilo)
        st.write(f"Huevo cósmico cargado: {egregor}")
        st.write("Creando contrato de magia caótica...")
        contrato = generar_contrato(usuario, self.nombre, descripcion)
        st.markdown(contrato, unsafe_allow_html=True)
        st.write("""
        **Debes proceder a imprimir el contrato y luego firmarlo, para luego quemarlo para terminar la activación. Suerte con tus invocaciones y visita [grimoriomagiadelcaos.blogspot.com](http://grimoriomagiadelcaos.blogspot.com) para más herramientas tecnomágicas.**
        """)

def cargar_egregore():
    # Simulación de carga de egregor
    return "El huevo cósmico es el medio que plantamos en el subconsciente, creciendo y alimentándose de nuestra magia interior. Aqui te descargas de la gnosis para cargar el servidor magico"

def seleccionar_servidor(servidores_magicos):
    servidor_seleccionado = st.selectbox("Selecciona el servidor mágico que deseas activar:", [servidor[0] for servidor in servidores_magicos])
    descripcion = next((desc for serv, desc in servidores_magicos if serv == servidor_seleccionado), None)
    return servidor_seleccionado, descripcion

def generar_sigilo(descripcion, usuario, pais):
    # Utilizando el generador de sigilos proporcionado
    sigilo = create_sigil(descripcion + usuario + pais)
    return sigilo

def generar_contrato(usuario, servidor, descripcion):
    contrato = f"""
    <div style="color: white; background-color: #660033; padding: 20px; border-radius: 10px;">
    <h2 style="text-align: center;">Invocación de {servidor}</h2>
    <p>Yo, <strong>{usuario}</strong>, con plena consciencia y voluntad, invoco al servidor mágico <strong>{servidor}</strong>. En este momento y lugar, te llamo desde las profundidades del caos, para que manifiestes tu poder y esencia en mi vida.</p>
    <p>Que tu presencia se haga sentir en cada aspecto de mi ser, y que tus dones se derramen sobre mí con abundancia y gracia. <strong>{servidor}</strong>, te invoco para que actúes en mi favor, guiando mis pasos y protegiéndome de todo mal.</p>
    <p>Este es mi pacto sagrado contigo:</p>
    <p>1. Te ofrezco mi respeto y mi reconocimiento como entidad poderosa y sabia.</p>
    <p>2. Comprometo mi energía y devoción en este ritual de invocación, entendiendo que el equilibrio y el intercambio son esenciales en la magia del caos.</p>
    <p>3. Declaro que mi intención es pura y alineada con los principios del caos, y que utilizaré tu poder de manera ética y responsable.</p>
    <p><strong>Descripción del Servidor:</strong> {descripcion}</p>
    <p><strong>{servidor}</strong>, escucha mi llamado:</p>
    <p><strong>{servidor}</strong>, desciende sobre mí.</p>
    <p><strong>{servidor}</strong>, manifiesta tu fuerza.</p>
    <p><strong>{servidor}</strong>, guía mi camino.</p>
    <p><strong>{servidor}</strong>, protege mi ser.</p>
    <p><strong>{servidor}</strong>, otorga tu sabiduría.</p>
    <p>Que este contrato quede sellado en el tiempo y el espacio, y que la energía que generamos juntos fluya hacia la realización de mis objetivos y deseos. Que así sea, y que así se manifieste.</p>
    <p>Firmado: {usuario}</p>
    </div>
    <br>
    """
    return contrato

def create_sigil(desire):
    consonants = [c for c in desire.lower() if c.isalpha() and c not in 'aeiou']
    letters = list(set(consonants))
    random.shuffle(letters)
    sigil = ''.join(letters)
    return sigil

def fibonacci_sphere(samples=1):
    rnd = 1.
    points = []
    offset = 2./samples
    increment = np.pi * (3. - np.sqrt(5.))
    for i in range(samples):
        y = ((i * offset) - 1) + (offset / 2)
        r = np.sqrt(1 - y*y)
        phi = ((i + rnd) % samples) * increment
        x = np.cos(phi) * r
        z = np.sin(phi) * r
        points.append([x, y, z])
    return points

def visualize_sigil(sigil):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_aspect('equal')
    ax.axis('off')
    circle = plt.Circle((0.5, 0.5), 0.4, color='black', fill=False, lw=2)
    ax.add_artist(circle)
    num_letters = len(sigil)
    fibonacci_points = fibonacci_sphere(num_letters)
    x_letters = [0.5 + 0.35 * p[0] for p in fibonacci_points]
    y_letters = [0.5 + 0.35 * p[1] for p in fibonacci_points]
    for i, letter in enumerate(sigil):
        ax.text(x_letters[i], y_letters[i], letter, fontsize=1, ha='center', va='center', color='black')
    for i in range(num_letters):
        j = (i + 1) % num_letters
        x_start, y_start = x_letters[i], y_letters[i]
        x_end, y_end = x_letters[j], y_letters[j]
        ax.plot([x_start, x_end], [y_start, y_end], color='black')
    ax.scatter(x_letters[0], y_letters[0], color='black', s=20)
    ax.scatter(x_letters[-1], y_letters[-1], color='black', s=20)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    st.pyplot(fig)

def main():
    st.set_page_config(page_title="Activador de Servidores Mágicos", layout="centered", initial_sidebar_state="expanded")

    st.title("Activador de Servidores Mágicos")
    st.markdown("---")
    st.write("Bienvenido al Activador de Servidores Mágicos.")
    st.write("Creado para el blog [grimoriomagiadelcaos.blogspot.com](http://grimoriomagiadelcaos.blogspot.com)")
    st.write("Por favor, completa la siguiente informacion para comenzar: ")

    usuario = st.text_input("Nombre o Alias del Mago:")
    pais = st.text_input("País de Origen del Mago:")
    
    if usuario and pais:
        servidores_magicos = [
    ("¡LOL!", "Servidor de la suerte y la amistad en juegos, físicos u online."),
    ("La Águila", "Protectora contra la violencia sexual."),
    ("La Banquera", "Experta en manejo financiero y apuestas."),
    ("Cupido", "Encargada de unir corazones y fomentar el amor."),
    ("La Curandera", "Especialista en resolver problemas de salud."),
    ("La Ilusionista", "Capaz de manipular los sueños según el deseo del evocador."),
    ("La Profesora", "Facilita el aprendizaje y el camino hacia el éxito académico."),
    ("La Suerte", "Brinda energía y determinación para alcanzar metas."),
    ("La Vengadora", "Representa la venganza y la oscuridad."),
    ("ABRALAS", "Facilitador de procesos y fluidez en la vida cotidiana."),
    ("Agromora", "Mejora las habilidades en masajes."),
    ("Aikendú", "Representa la luz, el equilibrio y la curación."),
    ("Alexia", "Elimina la depresión y la ansiedad."),
    ("Allie", "Resuelve problemas amorosos y sentimentales."),
    ("Alvo", "Manipula mentes, emociones y sueños."),
    ("Andaluz", "Cura aspectos psicológicos, físicos o emocionales."),
    ("Anya", "Experta en música y notas melódicas."),
    ("Applause", "Ayuda a artistas a prosperar en sus proyectos."),
    ("Aracne", "Elimina obstáculos en la vida del evocador."),
    ("Aristeia", "Promueve la eficiencia y la perfección."),
    ("Aros", "Aumenta la atracción y el deseo físico."),
    ("Artpop", "Atrae visibilidad y admiradores."),
    ("Arukah", "Deidad madre de la curación."),
    ("Aruspécia", "Auxilia en tiradas oraculares y estudios de adivinación."),
    ("Astron", "Protege a los animales y los guía de regreso a casa."),
    ("Aurore", "Combate traumas, miedos y fobias."),
    ("Avóh", "Transforma la tristeza en alegría y promueve el cambio positivo."),
    ("Billy, El Creador", "Estimula la creatividad y la inspiración."),
    ("Bonita", "Mejora la apariencia facial y capilar."),
    ("Califa", "Facilita el logro de metas a través de la energía sexual."),
    ("Calistrode", "Experta en ilusiones y alteraciones de la realidad."),
    ("Caote", "Combate la opresión y la injusticia."),
    ("Celeste", "Revela verdades ocultas y desenmascara mentiras."),
    ("Cereja", "Aumenta las probabilidades de cumplir deseos."),
    ("Cladris", "Promueve cambios positivos y transformaciones."),
    ("Cochichulupos", "Siente y manipula pensamientos y emociones."),
    ("Cognitionis", "Representa el saber y la verdad."),
    ("Cortana", "Especializada en banimento y limpieza energética."),
    ("Criativatura", "Extrae inspiración artística y energía creativa."),
    ("Ctônica", "Asiste en viajes oníricos y al submundo."),
    ("Dindorar", "Ayuda en asuntos financieros y de prosperidad."),
    ("Dominivince", "Aumenta las posibilidades de conseguir empleo."),
    ("Dorkus", "Mejora la belleza facial y corporal."),
    ("Elhos", "Refleja y neutraliza intenciones malignas."),
    ("Elo de Hélio", "Limpia energéticamente y alinea chakras."),
    ("Elon", "Expande la frecuencia y vibra energética positiva."),
    ("Erdwolf", "Despierta y fortalece el chamán interior."),
    ("Escarlate", "Incrementa la potencia sexual y la sensualidad."),
    ("ExuZen", "Equilibra la espiritualidad y lo terrenal."),
    ("Faster", "Acelera la manifestación de resultados."),
    ("Fotamecus", "Manipula la percepción del tiempo."),
    ("Fovadermos", "Atrae personas hacia el evocador."),
    ("Francis", "Veterinaria astral que cura animales."),
    ("Gabarita", "Facilita el éxito en pruebas y selecciones."),
    ("Gifty", "Facilita el envío y recepción de regalos."),
    ("Gloria", "Mejora la comunicación y la elegancia."),
    ("Grünewald", "Protege la flora y los espacios verdes."),
    ("Gueixa", "Protectora de artistas y su trabajo."),
    ("Harvem", "Promueve la salud y el bienestar."),
    ("Hazel", "Potencia los sueños lúcidos y vívidos."),
    ("Hímeros", "Encarna el deseo y la pasión victoriosa."),
    ("Holpe", "Combate la tristeza y la depresión."),
    ("Hrafna", "Ofrece apoyo emocional y espiritual."),
    ("JáTôLá", "Atrae eventos deseados hacia el evocador."),
    ("Jerdehl", "Favorece la prosperidad y la riqueza."),
    ("Jupi", "Brinda energía de Júpiter en cualquier momento."),
    ("Jupiturio Entraverba", "Abre posibilidades de ganancias inesperadas."),
    ("Justine", "Actúa como abogada astral."),
    ("Kaosciphéra Kuwantífera", "Hace lo imposible posible."),
    ("Kare", "Combate el coronavirus y el cambio climático."),
    ("Karuma Janai", "Desvía el karma negativo hacia la naturaleza."),
    ("Khundalina", "Aumenta la autoestima y la persuasión."),
    ("Kia", "Protege contra influencias negativas y ataques astrales."),
    ("Kneta", "Ayuda en el aprendizaje de idiomas."),
    ("Kranvoc", "Promueve la felicidad y el bienestar."),
    ("La Caliente", "Aumenta la autoestima y la sensualidad."),
    ("La Sagrada Mantis dela Suerte", "Atrae la suerte y elimina la mala suerte."),
    ("La Sombra", "Castiga y atormenta a sus víctimas."),
    ("Líndalë", "Asiste a músicos en su práctica y desafíos."),
    ("Liz", "Revela la verdad en situaciones ocultas."),
    ("Lu-Tero", "Manipula y controla energías sin necesidad de otras entidades."),
    ("Ludibriel", "Favorece en juegos de cartas como el póker."),
    (
        "Lunária",
        "Protege contra ataques astrales y facilita la comunicación entre mundos.",
    ),
    ("Lupran", "Revela, fortalece y promueve la fuerza interior."),
    ("Lux", "Promueve el confort material y el lujo."),
    ("Lux Titanus", "Limpia y transmuta energías densas."),
    ("Madremia", "Protege a hijos de madres narcisistas."),
    ("Magápe", "Manipula energías para decisiones favorables en casos judiciales."),
    ("Malia", "Protectora de animales abandonados."),
    ("Mani", "Especialista en belleza y salud estética."),
    ("Marmoon", "Aumenta la belleza, carisma y popularidad."),
    ("Mayat", "Realiza deseos amorosos del usuario."),
    ("Mel", "Aumenta la belleza y la autoestima."),
    ("Melíalpa", "Trae calma, equilibrio y paz mental."),
    ("Mercury", "Brinda energía de Mercurio en cualquier momento."),
    ("Metulza", "Encuentra personas compatibles para relaciones."),
    ("Mímico", "Hace que el operador se parezca a cualquier persona o personaje."),
    ("Misteriosa", "Oculta información y secretos."),
    ("Mnemófeus Lullaby", "Induce estados gnósticos en niños."),
    ("Modicrigar", "Facilita el aprendizaje de nuevos idiomas."),
    ("Moípô", "Oculta mentiras y revela la verdad."),
    ("Musy", "Asiste en todos los aspectos relacionados con la música."),
    ("My Mirror", "Realza la belleza y oculta imperfecciones."),
    ("Naitê Iru", "Equilibra y oculta emociones según el deseo del evocador."),
    ("Niro", "Mejora la memoria de los sueños y promueve la proyección astral."),
    ("Nketetudah", "Protector astral para viajes oníricos."),
    ("Noel", "Hija del Papá Noel que cumple deseos."),
    ("Novena", "Maldice y atormenta a sus víctimas."),
    ("Nuri", "Ayuda en casos de cólicos, TPN y relaciones íntimas."),
    ("O Arqueiro", "Defiende a minorías y manifestantes."),
    ("O Caotizador", "Ayuda en la práctica de la magia del caos."),
    ("O Fofurizador", "Aporta carisma, empatía y autoestima."),
    ("O Guarda Volumes", "Protege objetos importantes."),
    ("O Mercador", "Resuelve problemas y modifica la vida del evocador."),
    ("Octo", "Protege contra energías negativas."),
    ("Olhar Que Evitamos", "Ofrece nuevas perspectivas y visiones."),
    ("Oruttem", "Personalidad multifuncional para diferentes propósitos."),
    ("Phobosmariel", "Ataca y abre caminos hacia el objetivo del evocador."),
    ("Prospera", "Promueve la sabiduría para adquirir riquezas."),
    ("Psi", "Equilibra la salud mental y combate trastornos psicológicos."),
    ("Rabbi", "Ayuda en la cura de vicios."),
    ("Raziriel", "Convierte lo imposible en posible."),
    ("Regicida", "Combate la opresión sistemática."),
    ("Revol", "Revela dones espirituales y potencia rituales."),
    ("Rob Fire", "Anfitrión nocturno que garantiza la diversión y la seguridad."),
    ("Ronda", "Busca oportunidades financieras y dinero cercano."),
    ("Salekah", "Facilita la compra, venta o alquiler de propiedades."),
    ("Sallyu", "Aleja amistades o parejas no aprobadas."),
    ("Salvamariel", "Defiende al magista y neutraliza influencias externas."),
    ("Samuy", "Calma los ánimos y congela relaciones."),
    ("Saturnino", "Brinda energía de Saturno en cualquier momento."),
    ("Self", "Aumenta la autoestima y el autoconocimiento."),
    ("Sereia", "Atrapa con su canto magnético y atractivo."),
    ("Shastra Ganika", "Empodera en arte, ciencia y sexualidad."),
    ("Solicio", "Brinda energía del Sol en cualquier momento."),
    ("Soliloki", "Subcontrata otros Servos Astrales para realizar pedidos."),
    ("Sophia", "Equilibra y abre el Ajna para clarividencia."),
    ("Sr. Fortuna", "Servidor para prosperidad financiera."),
    (
        "Star Ajuda",
        "Ayuda en diversas áreas para mujeres, incluyendo salud, prosperidad y equilibrio emocional.",
    ),
    (
        "STAR MEE!",
        "Ideal para conquistar fama y popularidad, con conocimientos avanzados en marketing, imagen y psicología.",
    ),
    ("Starlight", "Ayuda a alcanzar éxito y prosperidad en cualquier situación."),
    ("Tecelão", "Multiplica el dinero gastado. el TECELÓN DEL DINERO."),
    ("TecnoMago", "Facilita el uso y la creación de herramientas tecnomágicas."),
    ("Terra", "Se encarga de todo lo relacionado al cultivo y cuidado de plantas."),
    ("Tévyah", "Enfocado en ganancias financieras, incluyendo juegos de lotería."),
    ("The Abundance", "Servidor astral para prosperidad financiera en diversas áreas."),
    ("The Adventurer - A Aventureira", "Fomenta la exploración y nuevas experiencias."),
    ("The Alice", "Despierta la sed de conocimiento constante."),
    ("The Alpha", "Concede características de liderazgo y seducción."),
    (
        "The Balancer - A Balanceadora",
        "Promueve mantener una vida equilibrada y armoniosa.",
    ),
    ("The Carnal - A Carnal", "Aceptación y positividad sobre la sexualidad."),
    ("The Chaste - A Casta", "Fomenta la disciplina y pureza."),
    ("The Conductor - O Maestro", "Ayuda a tomar control de la vida."),
    (
        "The Contemplator - O Contemplador",
        "Facilita el acceso al subconsciente para encontrar soluciones.",
    ),
    ("The Dancer - A Dançarina", "Promueve aceptar los fallos y cambios de planes."),
    ("The Daret", "Impulsa al amor propio y equilibrio."),
    ("The Dead - A Morta", "Conexión con antepasados y aprendizaje del pasado."),
    (
        "The Depleted - O Exaurido",
        "Reconocimiento de agotamiento y necesidad de recarga.",
    ),
    (
        "The Desperate - O Desesperado",
        "Representa el punto más bajo y la necesidad de cambio.",
    ),
    ("The Dev", "Mejora en juegos, desarrollo y creatividad."),
    ("The Devil - O Diabo", "Revela restricciones autoimpuestas."),
    ("The Djinn", "Cumple deseos."),
    ("The Explorer", "Promueve el crecimiento personal y auto-desarrollo."),
    ("The Eye - O Olho", "Reconoce la naturaleza de las cosas."),
    ("The Father - O Pai", "Ofrece orientación y sabiduría."),
    ("The Fixer - O Reparador", "Resuelve problemas con un costo."),
    ("The Fortunate - A Afortunada", "Promueve la felicidad, salud y prosperidad."),
    ("The Gate Keeper - O Guardião do Portal", "Tiene acceso a todas las puertas."),
    ("The Giver - O Doador", "Fomenta la generosidad y gratitud."),
    ("The Guru - O Guru", "Aplica conocimiento espiritual a la vida cotidiana."),
    ("The Headhunter", "Ayuda a conseguir trabajo y avance profesional."),
    ("The Healer - A Curandeira", "Enfocado en curación física y emocional."),
    ("The Idea - A Ideia", "Fomenta la creatividad y originalidad."),
    ("The Levitator - O Levitador", "Promueve la imparcialidad y desapego."),
    (
        "The Librarian - A Bibliotecária",
        "Fomenta el estudio y el aumento de conocimiento.",
    ),
    ("The Lightworker", "Purifica espacios y objetos mágicos."),
    ("The Lovely", "Aumenta la dulzura y el amor en una persona."),
    ("The Lovers - Os Enamorados", "Fomenta la conexión profunda en relaciones."),
    ("The Master - O Mestre", "Representa la versión más evolucionada de uno mismo."),
    ("The Media - A Mídia", "Destaca la importancia de la propaganda."),
    ("The Messenger - O Mensageiro", "Mejora la comunicación."),
    ("The Monk - O Monge", "Promueve la simplicidad y meditación."),
    ("The Moon - A Lua", "Revela verdades ocultas y autoengaños."),
    ("The Mother - A Mãe", "Promueve la seguridad y nutrición."),
    ("The Necklace", "Auxilia en asuntos financieros."),
    (
        "The Opposer - O Adversário",
        "Muestra restricciones externas y anima a enfrentarlas.",
    ),
    ("The Planet - O Planeta", "Recuerda nuestro lugar en la creación."),
    ("The Protector - O Protetor", "Ayuda a protegerse a sí mismo y a otros."),
    ("The Protester - A Manifestante", "Promueve la lucha contra la injusticia."),
    ("The Reate", "Proporciona reconciliación en relaciones."),
    ("The Repair", "Ayuda a reparar relaciones rotas."),
    (
        "The Road Opener - O Abridor de Caminhos",
        "Elimina obstáculos y abre oportunidades.",
    ),
    ("The Saint - O Santo", "Representa la intercesión y confianza en expertos."),
    ("The Seer - A Vidente", "Usa la intuición y guía interna."),
    ("The Sun - O Sol", "Muestra cómo brillar en todas las áreas de la vida."),
    ("The Thinker - O Pensador", "Fomenta el análisis e intelecto."),
    ("The Witch - A Bruxa", "Enfocada en la magia y hechicería."),
    ("Thorin", "Mejora habilidades en juegos y reflexos."),
    ("Triz", "Protege y elimina peligros."),
    ("Tulpa", "Atrae parejas o mejora la sensualidad."),
    ("Ugehtodai", "Ayuda a encontrar oportunidades laborales."),
    ("Vauhass", "Actúa sobre la memoria."),
    ("Venado de Siete Cuernos", "Enfocado en protección LGBT."),
    ("Venuziana", "Trae energía de Venus."),
    ("Veredicta", "Revela la verdad."),
    ("Vharmon", "Promueve sabiduría."),
    ("Viracéu", "Controla condiciones climáticas."),
    ("Xegrapralá", "Delimita y protege espacios."),
    ("Xoac", "Protege y cura sexualidad femenina."),
    ("ZesKia", "Encuentra gatos perdidos."),
    ("Zobaq", "Ataca a quienes cometen violencia."),
        ]

        egregor = cargar_egregore()

        servidor, descripcion = seleccionar_servidor(servidores_magicos)

        sigilo = generar_sigilo(descripcion, usuario, pais)

        st.write("Escoge tu servidor mágico y ENTRA EN GNOSIS CON ÉL! luego oprime el boton de GNOSIS ACTIVADA")
        if st.button("GNOSIS ACTIVADA"):
            servidor_magico = ServidorMagico(servidor)
            servidor_magico.activar(sigilo, egregor, usuario, descripcion)

if __name__ == "__main__":
    main()
