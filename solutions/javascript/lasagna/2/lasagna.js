
export const EXPECTED_MINUTES_IN_OVEN = 40;
export const preparation_time_perlayer=2;


export function remainingMinutesInOven(actualMinutesInOven) {
  return EXPECTED_MINUTES_IN_OVEN - actualMinutesInOven;
}


export function preparationTimeInMinutes(numberOfLayers) {
  return numberOfLayers * preparation_time_perlayer;
}


export function totalTimeInMinutes(numberOfLayers, actualMinutesInOven) {
  return preparationTimeInMinutes(numberOfLayers) + actualMinutesInOven;
}
