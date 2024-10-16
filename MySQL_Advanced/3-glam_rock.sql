-- script lists all bands ranked by longevity 

SELECT
  band_name,
  CASE
    WHEN split IS NULL THEN YEAR(CURDATE()) - formed
    ELSE split - formed
  END AS lifespan
FROM band
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;