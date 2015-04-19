CREATE TABLE IF NOT EXISTS `temperatures` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `temperature` double NOT NULL,
  `humidity` varchar(20) NOT NULL,
  `dateMeasured` date NOT NULL,
  `hourMeasured` int(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
