# beer-lambert-data-product


poetry install


`calibration curve of c over A: c = a0 + ( a1 * A)`

a1 = slope, an estimation of 1/EL
a0 = intercept, approaching 0


Assumptions: 


Calibration.csv file = 27 rows with 24 samples and 3 blanks 

Note: tests will fail if calibration.csv is updated to a file with a different row-count

1) data from SOP, each successive row corresponds to a successive timepoint. 
From the task description, we assume that if a run is going well that absorabance will increase at each timepoint. 
2) Assume when measuring multiple chemcial abosrances can be added together


To calibrate the absorptivity coefficient for each wavelength: 

A<sub>dilutedSample</sub> = l<sub>optical-path</sub> * (E<sub>sample</sub>C<sub>sample</sub> + E<sub>blank</sub>C<sub>blank</sub>)

E<sub>sample</sub> = ( (A<sub>dilutedSample</sub> / l<sub>optical-path</sub>)  - E<sub>blank</sub>C<sub>blank</sub> ) / C<sub>sample</sub>


Once calibrated, unknown sample concentration can be calculated from absorbance: 

A<sub>unknown-sample</sub> = l<sub>optical-path</sub> * (E<sub>calibrated-pigment</sub>C<sub>unknown-sample</sub> + E<sub>calibrated-blank</sub>C<sub>unknown-blank</sub>)

The relationship between concentrations of the pigment and blank: 

C<sub>unknown-sample</sub> + C<sub>unknown-blank</sub> = 50 mg/L


Assume intercept is zero

