
CREATE TABLE `etudiant` (
  `id_etudiant` int(20) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `nom` varchar(45) DEFAULT NULL,
  `niveau` varchar(45) DEFAULT NULL,
  `sexe` varchar(45) DEFAULT NULL,
  `dateNaissance` varchar(45) DEFAULT NULL,
  `lieuNaissance` varchar(50) NOT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `absence_semestre` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `presence` (
  `id` int(20) NOT NULL,
  `date` date NOT NULL,
  `seance` varchar(100) NOT NULL,
  `matiere` varchar(30) NOT NULL,
  `status` varchar(10) NOT NULL,
  `enseignant` varchar(100) NOT NULL,
  `idEtudiant` int(10) NOT NULL,
  `nomPrenomEtudiant` varchar(100) NOT NULL,
  `heureDebut` varchar(20) NOT NULL,
  `heureFin` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `presence`
--

INSERT INTO `presence` (`id`, `date`, `seance`, `matiere`, `status`, `enseignant`, `idEtudiant`, `nomPrenomEtudiant`, `heureDebut`, `heureFin`) VALUES
(59, '2023-01-11', 'TD', 'Telecoms', 'Présent', 'Monsieur Abdoukhadre Diop', 140, 'Marie DIOUF', '18:00', '19:00'),
(60, '2023-01-11', 'TD', 'Telecoms', 'Présent', 'Monsieur Abdoukhadre Diop', 140, 'Marie DIOUF', '18:00', '19:00');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `presence`
--
ALTER TABLE `presence`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `presence`
--
ALTER TABLE `presence`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;
COMMIT;