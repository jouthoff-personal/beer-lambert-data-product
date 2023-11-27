# beer-lambert-data-product

The Beer-Lambert Data Product generated predicted concentrations for sample pigment fermentation runs.

### Running the pipeline
In the package directory, run the following commands to calibrate a beer-lamber model and run predictions on samples.
```
poetry install
poetry run python main.py
```
Note: currently running into an issue with gdown which has stopped downloading fermentation data on my local machine. 
<url>https://github.com/jouthoff-personal/beer-lambert-data-product/issues/1 </url>


### Calibrating the model

A linear regression model is trained to estimate the absorptivity coefficient for given wavelength based on known concentration (c) and measured absorbance (A). 


<url>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8808104/ </url>

`calibration curve of c over A: c = a0 + ( a1 * A)`

a1 = slope, an estimation of 1/EL
a0 = intercept, approaching 0


## Assumptions: 
1) Assume a linear relationship between absorbance and concentration 
2) Assume no measuring effects/impacts 
3) Assume no interaction between blank and sample that would disproportionately impact the absorbance


To calculate the absorptivity coefficient for each wavelength: 

A<sub>dilutedSample</sub> = l<sub>optical-path</sub> * (E<sub>sample</sub>C<sub>sample</sub> + E<sub>blank</sub>C<sub>blank</sub>)

E<sub>sample</sub> = ( (A<sub>dilutedSample</sub> / l<sub>optical-path</sub>)  - E<sub>blank</sub>C<sub>blank</sub> ) / C<sub>sample</sub>


Once calibrated, unknown sample concentration can be calculated from absorbance: 

A<sub>unknown-sample</sub> = l<sub>optical-path</sub> * (E<sub>calibrated-pigment</sub>C<sub>unknown-sample</sub> + E<sub>calibrated-blank</sub>C<sub>unknown-blank</sub>)

The relationship between concentrations of the pigment and blank: 

C<sub>unknown-sample</sub> + C<sub>unknown-blank</sub> = 100% sample = 50 mg/L

C<sub>unknown-blank</sub> = ( 1 - C<sub>unknown-sample</sub> ) 

C<sub>unknown-sample</sub> =(  (A<sub>dilutedSample</sub> / l<sub>optical-path</sub>) - E<sub>blank</sub> ) / (E<sub>pigment</sub> -1 )

### Future Steps
1. Post model and prediction database to Notion API
2. Add data-cleanliness FLAG step to SOP data if that successive measurements increase in concentration (EXPECTED) or not (UNEXPECTED).
2. Include plots & visuals:
   3. Calibration curve plots for sets of wavelengths (i.e. 220-250 nm, 250-280nm ) to allow for visual inspection
   4. Plot predictions from each fermentation on calibration curve
5. Use blanks to calibrate model more effectively and to perform quality checks on the SOP data