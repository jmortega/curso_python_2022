--
-- Table structure for table `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `estudiantes`
--

INSERT INTO `estudiantes` (`name`, `email`, `phone`) VALUES
('student1', 'student1@gmail.com', '111111111'),
('student2', 'student2@gmail.com', '222222222'),
('student3', 'student3@gmail.com', '333333333'),
('student4', 'student4@gmail.com', '444444444');

