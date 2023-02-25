import { Origins } from '../../types/tunneller';
import STYLES from './ProfileEnlistment.module.scss';

type Props = {
    origins: Origins;
}

export function ProfileEnlistment({ origins }: Props) {
  return (
    <table className={STYLES.enlistment}>
      <tbody>
        <tr>
          <td>
            ENLISTMENT FORM
          </td>
        </tr>
        <tr>
          <th>
            Date of birth:
          </th>
          <td>
            {origins.birth.date.dayMonth}
            {' '}
            {origins.birth.date.year}
          </td>
        </tr>
        <tr>
          <th>
            Country of birth:
          </th>
          <td>
            {origins.birth.country}
          </td>
        </tr>
      </tbody>
    </table>
  );
}
