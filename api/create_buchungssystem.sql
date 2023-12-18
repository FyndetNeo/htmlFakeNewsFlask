-----------------------------------------------------------------------------
-- Erzeugt eine SQLite Testdatenbank.
-- 
-- Flask üblich wäre, diese Datei schema.sql zu nennen.
-- Siehe auch: https://flask.palletsprojects.com/en/2.3.x/tutorial/database/
--
-----------------------------------------------------------------------------

DROP TABLE IF EXISTS checkItGame;


CREATE TABLE checkItGame(
    checkGameId              INTEGER NOT NULL UNIQUE
,   text   TEXT NOT NULL
,   isTrue BOOLEAN NOT NULL
,   PRIMARY KEY (checkGameId)
);


INSERT INTO checkItGame (checkGameId, text, isTrue) VALUES
    (1, "Studies have recently discovered that drinking excessive amounts of energy drinks is actually good! Buy DRINK",    false)
,   (2, "Imagine this being like, a really well-written article. One that cites sources, has multiple reliable ones, that doesn''t sell you on anything.", true)
,   (3, "Studies have found that COBOL is the most efficient, well-made programming language", false)
;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS Scenes;

CREATE TABLE Scenes (
    sceneId INTEGER PRIMARY KEY AUTOINCREMENT,
    data JSON NOT NULL
);

INSERT INTO Scenes (data) VALUES
('{
  "currentVideo": "video1.mp4",
  "buttons": [
    {
      "buttonText": "Play Video 1",
      "nextVideo": "video2.mp4"
    },
    {
      "buttonText": "Play Video 2",
      "nextVideo": "video3.mp4"
    }
  ]
}'),
('{
  "currentVideo": "video2.mp4",
  "buttons": [
    {
      "buttonText": "Go to Scene 1",
      "nextChoice": {
        "currentVideo": "video1.mp4",
        "buttons": [
          {
            "buttonText": "Replay Video 1",
            "nextVideo": "video1.mp4"
          },
          {
            "buttonText": "Forward to Video 3",
            "nextVideo": "video3.mp4"
          }
        ]
      }
    },
    {
      "buttonText": "Play Video 4",
      "nextVideo": "video4.mp4"
    }
  ]
}');
